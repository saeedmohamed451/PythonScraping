#r "Microsoft.Azure.ApiHub.Sdk" 

using System;
using System.Net;
using Microsoft.Azure.ApiHub;

public class Contact
{
    // Each member corresponds to the column names in
    // the Google sheet.
    public string Retailer { get; set; }
    public string Location { get; set; }
    public string StoreAddress { get; set; }
    public string RetailerURL { get; set; }
    public string Grouping { get; set; }
    public string Suburb { get; set; }
    public string StoreCode { get; set; }
    public string ReleaseDay { get; set; }
    public string ReleaseTime { get; set; }
}


public static async Task<HttpResponseMessage> Run(HttpRequestMessage req, ITable<Contact> inputTable, Binder binder, TraceWriter log)
{
    ContinuationToken continuationToken = null;

    // Get the HTTP parameters.
    var queryString = req.GetQueryNameValuePairs();

    // Load the HTTP parameters into a dictionary.
    Dictionary<string, string> queryDictionary = queryString.ToDictionary(kv => kv.Key, kv=> kv.Value, StringComparer.OrdinalIgnoreCase);

    // Specifially interested in this HTTP parameter.
    var rowKey = "row";

    // Response to this HTTP request.
    var responseContent = "";

    // Row number interested in from the Google sheet.
    var rowNumberAsStr = ""; 

    // Extract the row number from the HTTP request.
    if (queryDictionary.TryGetValue(rowKey, out rowNumberAsStr))
    {
        responseContent = "Catalytic Scrape for Google Sheet Row: (" + rowNumberAsStr + ")";

        // Row number that the user has asked to be processed.
        int rowNumber = 0;

        // The row number was found on the Google sheet.
        bool foundRow = false;

        if (Int32.TryParse(rowNumberAsStr, out rowNumber))
        {
            // Keep track of the row number in the Google sheet.
            // We start the first row from this off-set.
            var rowCounter = 2;

            do
            {
                var segment = await inputTable.ListEntitiesAsync(continuationToken: continuationToken);
                foreach (var item in segment.Items)
                {
                    // Only interested in this specific row.
                    if (rowNumber == rowCounter)
                    {

                        // Update the response
                        responseContent += " (" + item.Retailer + "-" + item.Location + ")";
                        responseContent += " (" + item.Grouping + ")";

                        try
                        {
                            // Create a temporary name of a CSV file based on trigger.
                            string CSV_NAME = item.Retailer + "-" + item.Location + ".csv";

                            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();

                            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
                            startInfo.FileName = @"D:\home\site\wwwroot\venv\Scripts\python.exe";
                            startInfo.Arguments = @"D:\home\site\wwwroot\code\driveAzure.py ";
                            startInfo.Arguments += item.Retailer + " ";
                            startInfo.Arguments += item.Location + " ";
                            startInfo.Arguments += item.StoreAddress + " ";
                            startInfo.Arguments += item.RetailerURL + " ";
                            startInfo.Arguments += item.Grouping + " ";
			    startInfo.Arguments += item.Suburb + " ";
			    startInfo.Arguments += item.StoreCode;

                            startInfo.UseShellExecute = false;
                            startInfo.RedirectStandardOutput = true;

                            log.Info("-1--Kick-off Python Script---");

                            using(System.Diagnostics.Process process = System.Diagnostics.Process.Start(startInfo))
                            {
                                using(StreamReader reader = process.StandardOutput)
                                {
                                    string result = reader.ReadToEnd();
                                    // Report the python script output to the logs.
                                    log.Info(result);
				    responseContent += " (" + result + ")";
                                }
				// We can't wait because this can take a while.
				// Correct design pattern for this is to return a 202 Accepted response.
				//log.Info("Do not wait for python code to finish!");
				log.Info("Wait for python process to finish...");
				process.WaitForExit();
                            }

//                            // List all files in the CSV area.
//                            string [] fileEntries = Directory.GetFiles(@"D:\local\");
//                            foreach(string fileName in fileEntries)
//                            {
//                                // Can I read the file created by python?
//                                log.Info("Content of file from Python script...");
//                                log.Info(fileName);
//                                //log.Info(fileName.Replace("D:\local\", ""));
//                                //string text = System.IO.File.ReadAllText(@fileName);
//                                //var attributes = new Attribute[]
//                                //{
//                                //    // Must write to a container and full Azure data storage area.
//                                //    new BlobAttribute("azure-webjobs-hosts/" + fileName.Replace("D:\local\", "")),
//                                //    new StorageAccountAttribute("drivecatalyticsstorage_STORAGE")
//                                //};
//                                //// Now lets write to the Azure blob. 
//                                //using (var writer = await binder.BindAsync<TextWriter>(attributes))
//                                //{
//                                //    // log.Info(text);
//                                //    // Write some data to the blob.
//                                //    // writer.Write("This file is: " + CSV_NAME);
//                                //    // writer.Write(text);
//                                //}
//                                //
//                            }
                            log.Info("---Done---");
                        }
                        catch (Exception ex)
                        {
                            log.Info("Exception Found...");
                            log.Info(ex.ToString());
                        }


                        // No point going any further in this loop.
                        foundRow = true;
                        break;
                    }
                    rowCounter = rowCounter + 1;    
                }
                continuationToken = segment.ContinuationToken; ;
            }
            while (continuationToken != null);
        }

        // Row NOT found in Google sheet.
        if (!foundRow)
        {
            responseContent += " Unable to find row in Google sheet.";
        }
    }
    else
    {
        // No row parameter was found in the URL.
        responseContent = "Please specify a row number by including on the URL: &row=<number> for example &row=2 ";
    }

    // Final response to this request.
    // TODO: This should not be OK 200 but 202-Accepted!
    return req.CreateResponse(HttpStatusCode.OK, responseContent);
}
