
namespace DBmaintenance
{
    partial class Settings
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPageDBConnection = new System.Windows.Forms.TabPage();
            this.btnSettingsConnectionTest = new System.Windows.Forms.Button();
            this.txtSettingsPort = new System.Windows.Forms.TextBox();
            this.lblDBPort = new System.Windows.Forms.Label();
            this.txtSettingsDBNames = new System.Windows.Forms.TextBox();
            this.lblDBName = new System.Windows.Forms.Label();
            this.txtSettingsDBHost = new System.Windows.Forms.TextBox();
            this.lblDBHost = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.btnSettingsSave = new System.Windows.Forms.Button();
            this.btnSettingsCancel = new System.Windows.Forms.Button();
            this.lblSettingsOutput = new System.Windows.Forms.Label();
            this.tabControl1.SuspendLayout();
            this.tabPageDBConnection.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPageDBConnection);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Location = new System.Drawing.Point(12, 12);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(296, 194);
            this.tabControl1.TabIndex = 0;
            // 
            // tabPageDBConnection
            // 
            this.tabPageDBConnection.Controls.Add(this.lblSettingsOutput);
            this.tabPageDBConnection.Controls.Add(this.btnSettingsConnectionTest);
            this.tabPageDBConnection.Controls.Add(this.txtSettingsPort);
            this.tabPageDBConnection.Controls.Add(this.lblDBPort);
            this.tabPageDBConnection.Controls.Add(this.txtSettingsDBNames);
            this.tabPageDBConnection.Controls.Add(this.lblDBName);
            this.tabPageDBConnection.Controls.Add(this.txtSettingsDBHost);
            this.tabPageDBConnection.Controls.Add(this.lblDBHost);
            this.tabPageDBConnection.Location = new System.Drawing.Point(4, 22);
            this.tabPageDBConnection.Name = "tabPageDBConnection";
            this.tabPageDBConnection.Padding = new System.Windows.Forms.Padding(3);
            this.tabPageDBConnection.Size = new System.Drawing.Size(288, 168);
            this.tabPageDBConnection.TabIndex = 0;
            this.tabPageDBConnection.Text = "Database Connection";
            this.tabPageDBConnection.UseVisualStyleBackColor = true;
            // 
            // btnSettingsConnectionTest
            // 
            this.btnSettingsConnectionTest.Location = new System.Drawing.Point(180, 37);
            this.btnSettingsConnectionTest.Name = "btnSettingsConnectionTest";
            this.btnSettingsConnectionTest.Size = new System.Drawing.Size(102, 20);
            this.btnSettingsConnectionTest.TabIndex = 3;
            this.btnSettingsConnectionTest.Text = "Test connection";
            this.btnSettingsConnectionTest.UseVisualStyleBackColor = true;
            this.btnSettingsConnectionTest.Click += new System.EventHandler(this.btnSettingsTestConnection_Click);
            // 
            // txtSettingsPort
            // 
            this.txtSettingsPort.Location = new System.Drawing.Point(97, 37);
            this.txtSettingsPort.Name = "txtSettingsPort";
            this.txtSettingsPort.Size = new System.Drawing.Size(77, 20);
            this.txtSettingsPort.TabIndex = 2;
            this.txtSettingsPort.TextChanged += new System.EventHandler(this.textBox3_TextChanged);
            this.txtSettingsPort.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox3_KeyPress);
            // 
            // lblDBPort
            // 
            this.lblDBPort.AutoSize = true;
            this.lblDBPort.Location = new System.Drawing.Point(13, 40);
            this.lblDBPort.Name = "lblDBPort";
            this.lblDBPort.Size = new System.Drawing.Size(26, 13);
            this.lblDBPort.TabIndex = 4;
            this.lblDBPort.Text = "Port";
            // 
            // txtSettingsDBNames
            // 
            this.txtSettingsDBNames.Location = new System.Drawing.Point(97, 60);
            this.txtSettingsDBNames.Name = "txtSettingsDBNames";
            this.txtSettingsDBNames.Size = new System.Drawing.Size(76, 20);
            this.txtSettingsDBNames.TabIndex = 4;
            // 
            // lblDBName
            // 
            this.lblDBName.AutoSize = true;
            this.lblDBName.Location = new System.Drawing.Point(13, 63);
            this.lblDBName.Name = "lblDBName";
            this.lblDBName.Size = new System.Drawing.Size(84, 13);
            this.lblDBName.TabIndex = 2;
            this.lblDBName.Text = "Database Name";
            // 
            // txtSettingsDBHost
            // 
            this.txtSettingsDBHost.Location = new System.Drawing.Point(97, 15);
            this.txtSettingsDBHost.Name = "txtSettingsDBHost";
            this.txtSettingsDBHost.Size = new System.Drawing.Size(77, 20);
            this.txtSettingsDBHost.TabIndex = 1;
            // 
            // lblDBHost
            // 
            this.lblDBHost.AutoSize = true;
            this.lblDBHost.Location = new System.Drawing.Point(13, 18);
            this.lblDBHost.Name = "lblDBHost";
            this.lblDBHost.Size = new System.Drawing.Size(29, 13);
            this.lblDBHost.TabIndex = 0;
            this.lblDBHost.Text = "Host";
            // 
            // tabPage2
            // 
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(288, 168);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "tabPage2";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // btnSettingsSave
            // 
            this.btnSettingsSave.Location = new System.Drawing.Point(70, 212);
            this.btnSettingsSave.Name = "btnSettingsSave";
            this.btnSettingsSave.Size = new System.Drawing.Size(105, 30);
            this.btnSettingsSave.TabIndex = 1;
            this.btnSettingsSave.Text = "Save";
            this.btnSettingsSave.UseVisualStyleBackColor = true;
            // 
            // btnSettingsCancel
            // 
            this.btnSettingsCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnSettingsCancel.Location = new System.Drawing.Point(181, 212);
            this.btnSettingsCancel.Name = "btnSettingsCancel";
            this.btnSettingsCancel.Size = new System.Drawing.Size(105, 30);
            this.btnSettingsCancel.TabIndex = 2;
            this.btnSettingsCancel.Text = "Cancel";
            this.btnSettingsCancel.UseVisualStyleBackColor = true;
            this.btnSettingsCancel.Click += new System.EventHandler(this.btnSettingsCancel_Click);
            // 
            // lblSettingsOutput
            // 
            this.lblSettingsOutput.AutoSize = true;
            this.lblSettingsOutput.Location = new System.Drawing.Point(44, 94);
            this.lblSettingsOutput.Name = "lblSettingsOutput";
            this.lblSettingsOutput.Size = new System.Drawing.Size(0, 13);
            this.lblSettingsOutput.TabIndex = 5;
            // 
            // Settings
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.btnSettingsCancel;
            this.ClientSize = new System.Drawing.Size(320, 257);
            this.Controls.Add(this.btnSettingsCancel);
            this.Controls.Add(this.btnSettingsSave);
            this.Controls.Add(this.tabControl1);
            this.Name = "Settings";
            this.Text = "Settings";
            this.Load += new System.EventHandler(this.Settings_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPageDBConnection.ResumeLayout(false);
            this.tabPageDBConnection.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPageDBConnection;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Button btnSettingsSave;
        private System.Windows.Forms.Button btnSettingsCancel;
        private System.Windows.Forms.TextBox txtSettingsDBHost;
        private System.Windows.Forms.Label lblDBHost;
        private System.Windows.Forms.TextBox txtSettingsDBNames;
        private System.Windows.Forms.Label lblDBName;
        private System.Windows.Forms.TextBox txtSettingsPort;
        private System.Windows.Forms.Label lblDBPort;
        private System.Windows.Forms.Button btnSettingsConnectionTest;
        private System.Windows.Forms.Label lblSettingsOutput;
    }
}