<template>
  <div>
    <header>
      <h1>{{homeTitle}}</h1>   
         
      <button v-on:click="changename"> 만든이</button>  
      
    </header>
     
  </div>
</template>



<script>
export default {
  data(){
    return{
      homeTitle: "TODo_list"
    }
  },
  methods:{
    changename:function(event){
      alert('용태인')
      if(event){
        alert(event.target.tagName)
      }
    }
  }

}
</script>




<style scoped>                        
h1{
  color: #5d54e0;
  font-weight: 900;
  margin: 2.5rem 0 1.5rem;
}
button{
  color: rgb(119, 18, 18);
  background: rgb(236, 236, 70);
}

</style>
