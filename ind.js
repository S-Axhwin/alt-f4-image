const axios = require("axios");

(async() => {
    r = await fetch(response['url'], {
        method: 'POST',
        headers: {
            'Content-Type': 'multipart/form-data',
        },
        body: new FormData(),
    })
    console.log(await r.json());
})()
