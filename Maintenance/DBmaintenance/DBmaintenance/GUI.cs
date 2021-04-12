using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DBmaintenance
{
    public partial class GUI : Form
    {
        public GUI()
        {
            InitializeComponent();
        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void GUI_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Maximized;
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        Settings settings;

        private void settingsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            settings = new Settings();
            settings.MdiParent = this;
            settings.Show();

        }

        private void mnuHelpAbout_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Help");
        }
    }
}
