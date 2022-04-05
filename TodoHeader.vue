<template>
  <div>
    <header>
      <h1>{{homeTitle}}</h1>      
      <button v-on:click="changename"> 클릭시 변경</button>  
      
    </header>
     
  </div>
</template>



<script>
export default {
  data(){
    return{
      homeTitle: "Todo LIST (데이터 바인딩 으로 만듬))"
    }
  },
  methods:{
    changename:function(){
      this.homeTitle="TO DO 리스트"
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

</style>
