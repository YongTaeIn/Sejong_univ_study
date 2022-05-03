<!-- /src/Components/TodoFooter.vue -->

<template>
    <div>
        <button type="button" v-on:click="clearTodo">전체삭제</button>
        
    </div>
</template>

<script>
export default {
    methods: {
        clearTodo(){
            this.$emit('removeAll');
        }    
    }
}
</script>

<style scoped>
.clearAllContainer {
  width: 8.5rem;
  height: 50px;
  line-height: 50px;
  background-color: aqua;
  border-radius: 5px;
  margin: 0 auto;
}
.clearAllBtn {
  color: #2a9986;
  display: inline-block;
}
</style>