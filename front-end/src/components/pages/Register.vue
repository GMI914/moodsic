<template>
  <html>
    <head>
      <link rel="stylesheet" href="Login.css" />
    </head>

    <body>
      <div class="wrapper">
        <form class="login" action="server/login.php" method="post">
          <fieldset>
            <legend>Register</legend>
            <p>Username</p>
            <input type="text" name="user-name" />
            <p>Email</p>
            <input type="text" name="email" />
            <p>Password</p>
            <input type="password" name="password" />
            <p>Repeat Password</p>
            <input type="password" name="password-confirm" />
            <input type="submit" value="Proceed!" />
          </fieldset>
        </form>
      </div>
    </body>
  </html>
</template>

<script>
export default {};
</script>

<style scoped>
body {
  background-color: #262626;
}
.wrapper {
  width: 50%;
  background-color: #1a1a1d;
  position: relative;
  z-index: 0;
  margin: 0 auto;
  opacity: 0.91;
  padding: 3px;
}

form input[type="text"],
form select,
form textarea,
form input[type="password"] {
  width: 55%;
  display: block;
  padding: 5px;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 3px;
  margin-bottom: 9px;
  resize: vertical;
}

input[type="text"],
input[type="password"] {
  display: block;
  padding: 4px;
  margin: 3px;
  box-sizing: border-box;
  border: 2px solid #c3073f;
  background-color: #254f64;
  font-size: 21px;
  font-family: monospace, "Lucida Console";
  color: #ffff9b;
}

input[type="submit"] {
  background-color: #c3073f;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 7px;
}

form {
  margin: 0 auto;
}

p,
label {
  font-family: monospace, "Lucida Console";
  font-style: oblique;
  color: #05d9e8;
}

legend {
  font-family: monospace, "Lucida Console";
  font-style: oblique;
  font-size: 3em;
  font-weight: 300;
  line-height: 1em;
  text-align: center;
  color: #4dc3fa;
  text-shadow: 2px 2px red;
}
</style>

