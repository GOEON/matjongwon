<template>
  <div></div>
</template>

<script>
export default {
  methods: {
    getParameterByName: function(name) {
      console.log("getParameterByName");
      name = name.replace(/[[]/, "\\[").replace(/[\]]/, "\\]");
      var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
      return results == null
        ? ""
        : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
  },
  beforeMount() {
    console.log("beforeMount");
    const code = this.getParameterByName("code");

    alert(code);

    var details = {
      grant_type: "authorization_code",
      client_id: "381fdf3995c9049e5775ebb6242c1f15",
      redirect_uri: "http://localhost:8080/oauth/callback",
      code: code
    };

    var formBody = [];

    for (var property in details) {
      var encodedKey = encodeURIComponent(property);
      var encodedValue = encodeURIComponent(details[property]);
      formBody.push(encodedKey + "=" + encodedValue);
    }
    formBody = formBody.join("&");

    fetch("https://kauth.kakao.com/oauth/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
      },
      body: formBody
    })
      .then(response => response.json())
      .then(data => {
        console.log(JSON.stringify(data));
        alert(JSON.stringify(data));
        window.Kakao.Auth.setAccessToken(data.access_token);
        // test : Token
        alert(window.Kakao.Auth.getAccessToken());

        location.href = "/";
      });
  }
};
</script>
