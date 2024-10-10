import type { PageLoad } from "../$types";
import { error } from "@sveltejs/kit";

export const load: PageLoad = async ({ params }) => {
    try {
        const blogPost = await import(`../${params.slug}.md`);
        console.log(blogPost.metadata);
        const { title, date, publisher } = blogPost.metadata;
        const content = blogPost.default;

        return {
            content, 
            title,
            date,
            publisher
        };
    } catch (ex: any) {
        throw error(404, {
            message: ex.message
        })
    }
    
}