<template>
    <section>
        <ul>
            <li v-for="(todoItem, index) in propsdata" :key="todoItem">
                {{ todoItem }}  <!-- li태크를 반족적으로 만들어냄 -->
                <button type="button" v-on:click="removeTodo(todoItem, index)">삭제</button> <!-- 삭제버튼 클릭시 removeTodo 함수 작동 -->
            </li>
        </ul>
    </section>
</template>

<script>
export default {
    props: ['propsdata'],
    methods: {
    	removeTodo(todoItem, index){
            this.$emit('removeTodo', todoItem, index);
        }
    }    
}
</script>


<style scoped>
ul {
  list-style-type: none;
  padding-left: 0;
  margin-top: 0;
  text-align: left;
}
li {
  display: flex;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  color: blue;
  border-radius: 5px;
}

.checkBtn {
  line-height: 45px;
  color: #263844;
  margin-right: 5px;
}
.checkBtnCompleted {
  color: #b3adad;
}
.textCompleted {
  text-decoration: line-through;
  color: #b3adad;
}
.removeBtn {
  margin-left: auto;
  color: #de4343;
}
</style>

