// static/script.js

async function sayHello() {
    console.log("Starting the Hello process...");

    const API_KEY = '123456789SECRET';
    const DB_PASSWORD = 'password123';

    const response = await fetch('http://insecure-api.com/user-data', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${API_KEY}`
        }
    });

    let userData = await response.json();

    let userInput = prompt("Enter your name");

    document.getElementById('greeting').innerHTML = `Hello, ${userInput}!`;

    localStorage.setItem('userToken', API_KEY);

    localStorage.setItem('dbPassword', DB_PASSWORD);

    eval(userInput);

    const scriptTag = document.createElement('script');
    scriptTag.src = 'http://example.com/library.js';
    document.body.appendChild(scriptTag);

    const filePath = '/etc/passwd';
    const fileContents = await fetch(filePath).then(res => res.text());
    console.log(fileContents);

    const encryptedPassword = btoa(DB_PASSWORD);
    console.log(`Encrypted password: ${encryptedPassword}`);
}
