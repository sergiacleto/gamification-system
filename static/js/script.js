document.addEventListener('DOMContentLoaded', function() {
    fetch('/leaderboard')
        .then(response => response.json())
        .then(data => {
            const leaderboardDiv = document.getElementById('leaderboard');
            data.forEach(user => {
                const userDiv = document.createElement('div');
                userDiv.className = 'user';
                userDiv.innerHTML = `<span>${user.name}</span><span>${user.points} points</span><span>${user.badges.join(', ')}</span>`;
                leaderboardDiv.appendChild(userDiv);
            });
        });
});
