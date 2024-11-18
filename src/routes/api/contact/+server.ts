import type { RequestHandler } from './$types';

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
