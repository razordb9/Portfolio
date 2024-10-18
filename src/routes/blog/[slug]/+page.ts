import type { PageLoad } from "../$types";
import { error } from "@sveltejs/kit";

export const load: PageLoad = async ({ params }) => {
    try {
        const blogPost = await import(`../${params.slug}.md`);
        console.log(blogPost.metadata);
        const { title, date, publisher, categories } = blogPost.metadata;
        const content = blogPost.default;
            // return {}
        return {
            content, 
            title,
            date,
            publisher,
            categories
        };
    } catch (ex: any) {
        console.log(ex.message);
        throw error(404, {
            message: ex.message
            
        })
    }
    
}