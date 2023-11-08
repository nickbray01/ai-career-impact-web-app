<template>
    <div class="container">
        <h1>Will ai replace your job?</h1>
        <p class="paragraph">{{ intro_paragraph }}</p>
        <br>
        <v-row align="center" no-gutters>
            <v-col>
                <p>How will AI affect being a(n)</p>
            </v-col>
            <v-col>
                <v-text-field v-model="query" placeholder="occupation" density="compact"></v-text-field>
            </v-col>
            <v-col>
                <p> ?</p>
            </v-col>
            <v-col>
                <v-btn @click="askQuestion" class="btn btn-primary">Find out</v-btn>
            </v-col>
        </v-row>
        <p>{{ chat }}</p>
    </div>
    <v-card>
      <v-toolbar
        color="primary"
      >
        <v-toolbar-title>AI Impact Report</v-toolbar-title>
      </v-toolbar>
      <div class="d-flex flex-row">
        <v-tabs
          v-model="tab"
          direction="vertical"
          color="primary"
        >
          <v-tab value="option-1">
            <v-icon start>
              mdi-chart-areaspline
            </v-icon>
            Report Summary
          </v-tab>
          <v-tab value="option-2">
            <v-icon start>
              mdi-robot
            </v-icon>
            Human Specialties vs. AI Threats
          </v-tab>
          <v-tab value="option-3">
            <v-icon start>
              mdi-account-group
            </v-icon>
            Changing Coworkers
          </v-tab>
          <v-tab value="option-4">
            <v-icon start>
              mdi-wrench
            </v-icon>
            Future Proofing
          </v-tab>
        </v-tabs>
        <v-window v-model="tab">
          <v-window-item value="option-1">
            <v-card flat>
              <v-card-text>
                <p>
                  Sed aliquam ultrices mauris. Donec posuere vulputate arcu. Morbi ac felis. Etiam feugiat lorem non metus. Sed a libero.
                </p>
  
                <p>
                  Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Aliquam lobortis. Aliquam lobortis. Suspendisse non nisl sit amet velit hendrerit rutrum.
                </p>
  
                <p class="mb-0">
                  Phasellus dolor. Fusce neque. Fusce fermentum odio nec arcu. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Phasellus blandit leo ut odio.
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="option-2">
            <v-card flat>
              <v-card-text>
                <p>
                  Morbi nec metus. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
                </p>
  
                <p>
                  Suspendisse feugiat. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In hac habitasse platea dictumst. Fusce ac felis sit amet ligula pharetra condimentum.
                </p>
  
                <p>
                  Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Nam commodo suscipit quam. In consectetuer turpis ut velit. Sed cursus turpis vitae tortor. Aliquam eu nunc.
                </p>
  
                <p>
                  Etiam ut purus mattis mauris sodales aliquam. Ut varius tincidunt libero. Aenean viverra rhoncus pede. Duis leo. Fusce fermentum odio nec arcu.
                </p>
  
                <p class="mb-0">
                  Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="option-3">
            <v-card flat>
              <v-card-text>
                <p>
                  Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
                </p>
  
                <p class="mb-0">
                  Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
        </v-window>
      </div>
    </v-card>
  </template>
  
<script>
import axios from 'axios';
  
export default {
    data() {
        return {
            intro_paragraph: "Discover how AI might shape the future of your career! \
            Simply input your job title and receive personalized insights from an AI \
            career-impact consultant. Find out how artificial intelligence could impact \
            your profession in the upcoming years and get tailored advice on preparing for \
            these changes. Click here to gain valuable foresight and plan your career path \
            effectively.",
            chat: [],
            activeTab: 0,
            tabs: ['Report', 'Human Skills vs AI Threats', 'Changing Coworkers', 'Future-Proofing'],
            tab: 'option-1'
        };
    },
    methods: {
        askQuestion() {
            const path = 'http://localhost:5001/question';
            const payload = { prompt: this.query };
            axios.post(path, payload)
            .then((res) => {
                this.chat.push(res.data.query)
                this.chat.push(res.data.response)
            })
            .catch((error) => {
                console.log(error);
            })
        },
    }
}
</script>

<style>
.container {
    padding: 20px
}

.paragraph {
    color: gray;
}
</style>
