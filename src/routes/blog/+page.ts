export const load = async({fetch}) => {
    const respone = await fetch(`/api/posts`);
    const posts = await respone.json();

    console.log(posts);
    return {
        posts
    };
};