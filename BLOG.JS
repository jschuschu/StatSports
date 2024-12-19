// Select form and container elements
const postForm = document.getElementById('post-form');
const postsContainer = document.getElementById('posts-container');

// Handle form submission
postForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    // Get form values
    const password = document.getElementById('password').value;
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    // Check password
    if (password !== 'Wopu0956a') {
        alert('Incorrect password. You are not authorized to post.');
        return;
    }

    // Create a new post element
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `
        <h3>${title}</h3>
        <p>${content}</p>
        <button class="delete-button">Delete Post</button>
        <div class="comments-section">
            <h4>Comments</h4>
            <div class="comments-container"></div>
            <form class="comment-form">
                <input type="text" class="comment-username" placeholder="Enter your username" required>
                <input type="text" class="comment-content" placeholder="Write a comment..." required>
                <button type="submit">Add Comment</button>
            </form>
        </div>
    `;

    // Add the post to the container
    postsContainer.appendChild(post);

    // Clear the form
    postForm.reset();

    // Add delete functionality to the button
    const deleteButton = post.querySelector('.delete-button');
    deleteButton.addEventListener('click', () => {
        post.remove(); // Remove the post
    });

    // Add comment functionality
    const commentForm = post.querySelector('.comment-form');
    const commentsContainer = post.querySelector('.comments-container');

    commentForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form submission

        // Get username and comment input
        const usernameInput = commentForm.querySelector('.comment-username');
        const commentInput = commentForm.querySelector('.comment-content');

        // Check if username and comment are provided
        if (usernameInput.value.trim() === '' || commentInput.value.trim() === '') {
            alert('Please enter both a username and a comment.');
            return;
        }

        // Create a comment element
        const comment = document.createElement('div');
        comment.className = 'comment';
        comment.innerHTML = `
            <strong>${usernameInput.value}:</strong> ${commentInput.value}
        `;

        // Add the comment to the comments container
        commentsContainer.appendChild(comment);

        // Clear the input fields
        usernameInput.value = '';
        commentInput.value = '';
    });
});

