using System;

using Google.Cloud.Language.V1;

namespace NaturalLanguageApiDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            var text = "Yukihiro Matsumoto is great!";
            var client = LanguageServiceClient.Create();
            var response = client.AnalyzeSentiment(Document.FromPlainText(text));
            var sentiment = response.DocumentSentiment;
            Console.WriteLine($"Score: {sentiment.Score}");
            Console.WriteLine($"Magnitude: {sentiment.Magnitude}");
        }
    }
}
