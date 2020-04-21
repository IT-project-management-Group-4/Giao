function login() {

    var username = document.getElementById("username");
    var pass = document.getElementById("password");

    if (username.value == "") {

        alert("请输入用户名,僵尸吃掉了你的脑子！");

    } else if (pass.value  == "") {

        alert("请输入密码，僵尸吃掉了你的脑子！");

    } else if(username.value == "admin" && pass.value == "123456"){

        alert("歪比巴卜恭喜您登陆成功!");

    } else {

        alert("请输入正确的用户名和密码，僵尸吃掉了你的脑子！")

    }
}