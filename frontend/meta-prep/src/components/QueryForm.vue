<template>
    <div class="container">
        <h2> SQL Query Practice </h2>
        <textarea v-model="query" placeholder="Enter SQL Query here..." rows="5"></textarea>
        <button @click="submitQuery">Run Query</button>
        <p v-if="error" style="color: red;"> {{ error }}</p>
        <div v-if="results.length > 0">
            <h3>Results:</h3>
            <pre> {{ results }}</pre>
        </div>
        <div v-if="questions.length > 0">
            <h3>Questions:</h3>
            <ul>
                <li v-for="question in questions" :key="question.id">
                    {{ question.question }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            query: '',
            results: [],
            error: '',
            questions: []
        };
    },
    async mounted() {
        try {
            const response = await axios.get('http://localhost:5000/questions');
            console.log('loaded questions:', response.data);
            this.questions = response.data;
        } catch (err) {
            console.error('Error fetching questions:', err);
            this.error = 'An error occurred while fetching questions.';
        }
    },
    methods: {
        async submitQuery() {
            this.error = '';
            this.results = [];
            try {
                const response = await axios.post('http://localhost:5000/execute', { query: this.query });
                if (response.data.success) {
                    this.results = response.data.result;
                } else {
                    this.error = response.data.error;
                }
            } catch (err) {
                console.error('Error executing query:', err);
                this.error = 'An error occurred while executing the query.';
            }
        }
    }
};
</script>