// // // const nome = "Matheus"
// // // function hello(nome){
// // //     return `Olá ${nome}`
// // // }

// // // let salute = hello(nome)

// // // console.log(salute)

// // // Calculadora
// // // (+) (-) (/) (*) (**)
// // function soma(termo1, termo2){
// //     return termo1+termo2
// // }

// // function subtraction(termo1,termo2){
// //     return termo1-termo2
// // }

// // function divide(termo1,termo2){
// //     return termo1/termo2
// // }

// // function multiplication(termo1,termo2){
// //     if(termo2 === 0){
// //         return "Divisão por zero não é possível."
// //     }
// //     return termo1*termo2
// // }

// // function expo(termo1,termo2){
// //     if(termo1 ===0){
// //         return "Eita nóis, n sei fazer isso não"
// //     }
// //     if(termo2 === 0){
// //         return "Eita, piorou"
// //     }
// //     return termo1**termo2
// // }

// // const resultado = soma(1,2)

// // const resultado2 = subtraction(2,4)

// // const resultado3 = divide(5,5)

// // const resultado4 = multiplication(10,0)

// // const resultado5 = expo  (0,0)


// // console.log(resultado)
// // console.log(resultado2)
// // console.log(resultado3)
// // console.log(resultado4)
// // console.log(resultado5)

// function calculadora(termo1,operacao,termo2){
//     const operacaolowercase = operacao.toLowerCase()
//     switch(operacaolowercase){
//     case"mais":
//         return termo1+termo2
      
//     case"menos":
//         return termo1-termo2
        
//     case"vezes":
//         return termo1*termo2
      
//     case"dividido":
//         return termo1/termo2
//     case"potencia":
//         return termo1**termo2
    
//     default:
//         return "Operação não permitida"
//     }


// }

// const resultado = calculadora(1,"VEZES",1)
// console.log(resultado)

// CRUD

// let comidas = ["burguer","ovos", "pizza"]

// comidas.push("rabanada")

// console.log(comidas[3])

// comidas.pop()
// console.log(comidas[3])


let todolist=[]
function createtask(nome){
    todolist.push(nome)
}

function readtask(){
    console.log(todolist)
}

todolist.findIndex((element)=>{
return element === "dar comida à gata"
})
createtask("dar comida pra kiki")
function encontrarindicepelonome(nome){
    const index = todolist.findIndex(function(element){
        return element === none 
    })
    return index
}
const tarefas =readtask
console.log(todolist)