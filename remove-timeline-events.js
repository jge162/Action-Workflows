const axios = require('axios');

async function removeEvents() {
  const authToken = 'YOUR_PERSONAL_ACCESS_TOKEN';
  const prNumber = process.argv[2];
  const owner = process.env.GITHUB_REPOSITORY_OWNER;
  const repo = process.env.GITHUB_REPOSITORY;

  try {
    if (prNumber) {
      // Fetch comments for the pull request
      const response = await axios.get(`https://api.github.com/repos/${owner}/${repo}/issues/${prNumber}/comments`, {
        headers: {
          Authorization: `Bearer ${authToken}`,
        },
      });

      // Delete the comments made by the GitHub Actions bot
      for (const comment of response.data) {
        if (comment.user.type === 'Bot' && comment.user.login === 'github-actions[bot]') {
          await axios.delete(`https://api.github.com/repos/${owner}/${repo}/issues/comments/${comment.id}`, {
            headers: {
              Authorization: `Bearer ${authToken}`,
            },
          });
        }
      }
    } else {
      console.log('Not a pull request event or missing pull request number. Skipping comment removal.');
    }
  } catch (error) {
    console.error('Error removing comments:', error);
    throw error;
  }
}

removeEvents();
