const axios = require('axios');
const cron = require('node-cron');

// Function to execute the API call
async function executeAPI() {
    try {
        const response = await axios.get('https://nayeraa-techtrackapi.hf.space/run-notebook'); 
        console.log(response.data);
    } catch (error) {
        console.error('Error executing API:', error.message);
    }
}

// Schedule the API call to execute every day at midnight
cron.schedule('0 0 * * *', () => {
    console.log('Executing API call...');
    executeAPI();
});
