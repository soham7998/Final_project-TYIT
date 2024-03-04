function cookiemail() {
    console.log("hello world");
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    document.cookie = `username=${username}; email=${email}; password=${password}`;
    console.log(document.cookie);
}
