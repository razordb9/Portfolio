using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Driver;
using MongoDB.Bson;
using System.Windows.Forms;

namespace DBmaintenance
{
    class Program
    {
        static void Main(string[] args)
        {
            MongoClient dbClient = new MongoClient("mongodb://127.0.0.1");

            //List all db's on a specific server
            var dbList = dbClient.ListDatabases().ToList();
            Console.WriteLine("The list of databases on this server is: ");
            foreach (var db in dbList)
            {
                Console.WriteLine(db);
            }
            var database = dbClient.GetDatabase("PortFolio");

            var selectCollection = database.GetCollection<BsonDocument>("Permission");

            //List all collections for specific db
            var collectionList = database.ListCollections().ToList();
            Console.WriteLine("The list of collections for db: ");
            foreach (var item in collectionList)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            //Read Data from specific collection
            var documents = selectCollection.Find(new BsonDocument()).ToList();


            //Create new entry in specific collection
            var permissionDoc = new BsonDocument
            {
                {"permission_id", 4 },
                {"permission", "SA" }
            };

            //selectCollection.InsertOne(permissionDoc);

            //documents.ForEach(doc => { Console.WriteLine(doc.ToString()); });


            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new GUI());
        }
    }
}
