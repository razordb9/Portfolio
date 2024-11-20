import type { RequestHandler } from './$types';
import nodemailer from 'nodemailer';

export const POST: RequestHandler = async ({ request }) => {
  try {
    const { name, email, message } = await request.json();

    if (!name || !email || !message) {
      return new Response(
        JSON.stringify({ message: 'All fields are required.' }),
        { status: 400 }
      );
    }

    // Here, you can send the data to a database, email service, etc.

    console.log({ name, email, message });

    const transporter = nodemailer.createTransport({
      host: "smtp.gmail.com",
      port: 587,
      secure: false, // true for port 465, false for other ports
      auth: {
        user: "thomas.zaussnig@gmail.com",
        pass: "aiju vvaj zsqk cnkb",
      },
    });

    transporter.sendMail({
      from: 'thomas.zaussnig@gmail.com', // sender address
      to: "thomas.zaussnig@gmail.com", // list of receivers
      subject: "ContactForm", // Subject line
      text: message // html body
    })

    return new Response(
      JSON.stringify({ message: 'Message received successfully!' }),
      { status: 200 }
    );
  } catch (error) {
    return new Response(
      JSON.stringify({ message: 'Error processing your request.' }),
      { status: 500 }
    );
  }
};
