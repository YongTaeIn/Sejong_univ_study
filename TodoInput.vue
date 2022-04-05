<template>
  <div>
   
    <input type="text" v-model="newTodoItem" v-on:keyup.enter="addTodo">
    <button v-on:click="addTodo">추가</button>
  </div>
</template>

<script>
export default {
  data(){
    return{
      newTodoItem:''
    }
  },
  methods: {
    addTodo: function() {
      console.log(this.newTodoItem);
      //저장하는 로직
      localStorage.setItem(this.newTodoItem, this.newTodoItem);
      this.clearInput();
    },
    clearInput: function() {
      this.newTodoItem=""; //비워주기(초기화)
    }
  }
}
</script>

<style>

</style>
