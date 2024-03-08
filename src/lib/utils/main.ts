import { resolve } from "path";



export const fetchPosts = async() => {
    const mdFiles = import.meta.glob('/src/routes/blog/*.md');
    const mdFilesIterable = Object.entries(mdFiles);
    const allPosts = await Promise.all(
        mdFilesIterable.map(async ([path, resolver]) => {
            const meta:any = await resolver();
            const postPath = path.slice(11, -3);
            return {
                meta: meta.metadata,
                path: postPath
            };
        })
    );
    
    return allPosts;
}