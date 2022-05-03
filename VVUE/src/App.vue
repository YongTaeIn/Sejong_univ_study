<template>
    <div id="app">
        <TodoHeader></TodoHeader>
        <TodoInput v-on:addTodo="addTodo"></TodoInput>
        <TodoList v-bind:propsdata="todoItems" v-on:removeTodo="removeTodo"></TodoList>
        <TodoFooter v-on:removeAll="clearAll"></TodoFooter>
        
    </div>


</template>

<script>
import TodoHeader from './components/TodoHeader';
import TodoInput from './components/TodoInput';
import TodoList from './components/TodoList';
import TodoFooter from './components/TodoFooter';


export default {
    data(){
        return {
            todoItems: []
        }
    },
    created: function() { 
    if (localStorage.length > 0) {
      for (var i = 0; i < localStorage.length; i++) {
        if (localStorage.key(i) !== 'loglevel:webpack-dev-server') {
          this.todoItems.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
        }
      }
    }
  },
    methods: {
        addTodo(todoItem){
            //로컬스토리지에 데이터를 추가하는 로직
            localStorage.setItem(todoItem, todoItem);
            this.todoItems.push(todoItem);
        },
        removeTodo(todoItem, index) {
            //각각 삭제 하는 역할.                 
            localStorage.removeItem(todoItem);
            this.todoItems.splice(index, 1);
        },
        clearAll(){
            //로컬스토리지 전체 삭제, todoItems 초기화
            localStorage.clear();
            this.todoItems = [];
        }
    },    
    components: {
        'TodoHeader': TodoHeader,
        'TodoInput': TodoInput,
        'TodoList': TodoList,
        'TodoFooter': TodoFooter
    }
}
</script>


<style>
  body{
  text-align: center;
  background-color: #9880db;
  }
  input{
  border-style: groove;
  width: 200px
}
  button{
    border-style: groove;
  }
  .shadow{
  box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03)
  }
</style>
