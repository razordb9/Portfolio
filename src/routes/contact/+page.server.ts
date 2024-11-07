import type { Actions } from './$types';

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.json();
    const { name, email, message } = data;

    // Simple validation
    if (!name || !email || !message) {
      return {
        status: 400,
        body: { message: 'All fields are required.' }
      };
    }

    // (Optional) Here you would typically process the form data, such as:
    // - Send it to a database
    // - Send an email using an email API
    // - etc.

    // Mock response
    return {
      status: 200,
      body: { message: 'Thank you for contacting us!' }
    };
  }
};
