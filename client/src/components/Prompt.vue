<template>
    <div class="container">
        <h1>Will ai replace your job?</h1>
        <h3>A report compiled by ai</h3>
        <p class="paragraph">{{ introParagraph }}</p>
        <br>
        <v-row allign="center" no-gutters>
            <v-col>
                <p>How will AI affect being a(n)</p>
            </v-col>
            <v-col>
                <v-text-field v-model="occupation" placeholder="occupation" density="compact" :disabled="occupationDisabled"></v-text-field>
            </v-col>
            <v-col>
                <p> ?</p>
            </v-col>
            <v-col>
                <v-btn @click="fillReport" class="btn btn-primary" :disabled="occupationDisabled">Find out</v-btn>
            </v-col>
        </v-row>
    </div>
    <v-alert color="error" icon="$error" v-show="error" :title="errorTitle" :text="errorText">
    </v-alert>
    <v-card v-show="validOccupation">
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
          <v-tab value="summary">
            <v-icon start>
              mdi-chart-areaspline
            </v-icon>
            Report Summary
          </v-tab>
          <v-tab value="humanity">
            <v-icon start>
              mdi-account
            </v-icon>
            Unique Human Talents
          </v-tab>
          <v-tab value="aiThreats">
            <v-icon start>
              mdi-robot
            </v-icon>
            AI Threats
          </v-tab>
          <v-tab value="coworkers">
            <v-icon start>
              mdi-account-group
            </v-icon>
            Changing Coworkers
          </v-tab>
          <v-tab value="upskill">
            <v-icon start>
              mdi-wrench
            </v-icon>
            Future Proofing
          </v-tab>
        </v-tabs>
        <v-window v-model="tab">
          <v-window-item value="summary">
            <v-card flat>
              <v-card-text>
                <h2>How ai will impact a {{ aiOccupation }}</h2>
                <p>
                    {{ summaryText }}
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="humanity">
            <v-card flat>
              <v-card-text>
                <p>
                    {{ humanityText }}
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="aiThreats">
            <v-card flat>
              <v-card-text>
                <p>
                    {{ aiThreatsText }}
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="coworkers">
            <v-card flat>
              <v-card-text>
                <p>
                    {{ coworkersText }}
                </p>
              </v-card-text>
            </v-card>
          </v-window-item>
          <v-window-item value="upskill">
            <v-card flat>
              <v-card-text>
                <p>
                    {{ upskillText }}
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
            introParagraph: 'Discover how AI might shape the future of your career! \
            Simply input your job title and receive personalized insights from an AI \
            career-impact consultant. Find out how artificial intelligence could impact \
            your profession in the upcoming years and get tailored advice on preparing for \
            these changes. Click here to gain valuable foresight and plan your career path \
            effectively.',
            occupation: '',
            aiOccupation: '',
            occupationDisabled: false,
            validOccupation: false,
            error: false,
            errorTitle: '',
            errorText: '',
            summaryText: '',
            humanityText: '',
            aiThreatsText: '',
            coworkersText: '',
            upskillText: '',
            activeTab: 0,
            tab: 'summary'
        };
    },
    methods: {
        // Generic Questions to the ai bot w/ no server-side prompt engineering
        askQuestion() {
            const path = 'http://localhost:5001/ask-ai';
            const payload = { prompt: this.query };
            axios.post(path, payload)
            .then((res) => {
                this.summaryText = res.data.response
            })
            .catch((error) => {
                console.log(error);
            })
        },
        // Confirm that the user entered a valid occupation
        async validateOccupation() {
            try {
                this.occupationDisabled = true;
                this.error = false;
                const path = 'http://localhost:5001/validate-occupation';
                const payload = { occupation: this.occupation };
                const response = await axios.post(path, payload);
                this.aiOccupation = response.data.response;

                if (this.aiOccupation !== "invalid job") {
                    this.validOccupation = true;
                } else {
                    console.log("Invalid occupation selected.");
                    this.occupationDisabled = false;
                    this.errorTitle = "Invalid Occupation";
                    this.errorText = "I am unable to generate an occupational risk report for " + this.occupation;
                    this.error = true;
                }
            } catch (error) {
                console.log(error);
                this.occupationDisabled = false;
                this.errorTitle = "Error";
                this.errorText = "Unable to connect to the server.";
                this.error = true;
            }
            return this.validOccupation;
        },

        async fillReport() {
            const isValid = await this.validateOccupation();
            if (isValid) {
                this.fillParagraph("summary-intro");
            }
            console.log(this.validOccupation);
        },

        async fillParagraph(section) {
            try {
                const path = 'http://localhost:5001/fill-paragraph';
                const payload = { occupation: this.occupation, section: section };
                const response = await axios.post(path, payload);
                this.summaryText = response.data.response;
            } catch (error) {
                console.log(error);
            }
        }
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
