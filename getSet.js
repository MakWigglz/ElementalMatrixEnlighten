class UserChoice {
    contstructor() {
        this._choice = '';
    }
    get choice() {
        return this._choice;
    }
    set choice(value) {
        this._set_choice = value;
        // Send the choice to the server
        fetch('/set_choice', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({ choice: this._choice})

        })
        .then(response => response.json())
        .then(data => {
            console.log('server response:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
//Example usage
const userChoice = new UserChoice();
document.querySelector('#learningButton').addEventListener('click', () => {
    userChoice.choice = 'learning';
});
document.querySelector('#warButton').addEventListener('click', () => {
    userChoice.choice = 'war';
});