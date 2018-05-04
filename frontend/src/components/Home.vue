import axios from 'axios'

<template>
  <div>
    <p>Home Page</p>
	<p>Random Song From Backend: {{ randomSong }}</p>
    <button @click="getRandom">New Random Song</button>
  </div>
</template>  

<script>
/* eslint-disable */

export default {
  data () {
    return {
      randomSong: 'Smokestack Lightning, Key of C'
    }
  },
  methods: {
    getRandomChoice (songs) {
	songs = ['Little Red Rooster, Key of G', 'Basic 12-bar Blues, Any Key', 'Should I Stay or Should I Go?, Key of E']
	return random.choice(songs)
	},
    getRandom () {
      this.randomSong = this.getRandomChoice(songs)
    }
  },
  getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
      .then(response => {
        this.randomSong = response.data.randomSong
      })
      .catch(error => {
        console.log(error)
      })
    }
  }  
</script>
