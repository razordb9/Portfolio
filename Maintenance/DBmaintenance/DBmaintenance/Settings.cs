using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MongoDB.Driver;
using MongoDB.Bson;

namespace DBmaintenance
{
    public partial class Settings : Form
    {
        public Settings()
        {
            InitializeComponent();
        }

        private void btnSettingsCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Settings_Load(object sender, EventArgs e)
        {
            ControlBox = false;
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            //e.Handled = !char.IsDigit(e.KeyChar) && !char.IsControl(e.KeyChar);
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            //Checks if input are only numbers
            e.Handled = !char.IsDigit(e.KeyChar) && !char.IsControl(e.KeyChar);
        }

        private void btnSettingsTestConnection_Click(object sender, EventArgs e)
        {
            if (String.IsNullOrEmpty(txtSettingsDBHost.Text) && (String.IsNullOrEmpty(txtSettingsPort.Text)))
            {
                MessageBox.Show("Hostname missing");
                MessageBox.Show("Port missing");
            }
            else if ((String.IsNullOrEmpty(txtSettingsDBHost.Text)))
            {

                MessageBox.Show("Hostname missing");
            }
            else if (String.IsNullOrEmpty(txtSettingsPort.Text))
            {
                MessageBox.Show("Port missing");
            } else
            {
                string dbHost = txtSettingsDBHost.Text;
                string dbPort = txtSettingsPort.Text;
                string dbConnect = "\"mongodb://" + dbHost + "\"";
                MessageBox.Show(dbConnect);
                //MongoClient dbClient = new MongoClient(dbConnect);
                MongoClient dbClient = new MongoClient("mongodb://127.0.0.1");
                var dbList = dbClient.ListDatabases().ToList();

                //foreach (char db in dbList)
                //{
                //    MessageBox.Show(db);
                //}
                  
            }


            //string dbHost = txtSettingsDBHost.Text;
            //string dbPort = txtSettingsPort.Text;
            //MessageBox.Show("\"mongodb:" + dbHost + ":" + dbPort);

            /*MongoClient dbClient = new MongoClient("mongodb://127.0.0.1");

            var dbList = dbClient.ListDatabases().ToList();

            foreach (var db in dbList)
            {
                MessageBox.Show((string)db);
            }
            */
        }
    }
}
