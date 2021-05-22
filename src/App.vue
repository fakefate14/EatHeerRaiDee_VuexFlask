<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="data:image/jpeg;base64,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"
          transition="scale-transition"
          width="50"
        />
        <div><h1>แดกอะไรดีวะไอสัส</h1></div>
      </div>

      <v-spacer></v-spacer>
      <div><h1>ไอสัสแดกอะไรดีวะ</h1></div>
    </v-app-bar>

    <v-main>
      <v-container grid-list-xs>
        <v-row>
          <v-col> </v-col>
          <v-col>
            <v-btn @click="AlertX" elevation="2">แดกอะไรดี</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <div v-if="foodShow">
              <v-alert border="bottom" color="pink darken-1" dark prominent>
                <v-container>
                  <v-row>
                    <div v-for="(item, index) in Foods" :key="index">
                       กูแนะนำให้มึงแดก {{ item.name }} เป็นอันดับที่ {{index+1}}
                      <v-col>
                        <v-img
                          :src="item.url"
                          alt="Vuetify Logo"
                          class="shrink mr-2"
                          contain
                          transition="scale-transition"
                          width="500"

                        >
                        </v-img>
                      </v-col>
                    </div>
                  </v-row>
                </v-container>
              </v-alert>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "App",

  components: {},
  data() {
    return {
      testUrl:
        "https://www.haveazeed.com/wp-content/uploads/2019/08/3.%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%9C%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B8%A1%E0%B8%B9-1.png",
      Food: {
        name: "",
        url:
          "https://www.haveazeed.com/wp-content/uploads/2019/08/3.%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%9C%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B8%A1%E0%B8%B9-1.png",
      },
      foodShow: false,
      Foods: [],
    };
  },
  methods: {
    // header(“Access-Control-Allow-Origin: *”);
    async AlertX() {
      this.foodShow = false;
      const config = {
        method: "get",
        url: "http://127.0.0.1:5000/eat",
      };
      let res = await axios(config);
      // console.log(res.data["message"][0]["name"]);
      // console.log(res.data["message"][0]["url"]);

      this.Food.name = res.data["message"];
      this.Food.url = res.data["message"];
      this.Foods = res.data["message"];
      // console.log()
      this.foodShow = true;
    },
  },
};
</script>
