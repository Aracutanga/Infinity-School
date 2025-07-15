let idade = Number(prompt("Digite a sua idade: "))
if(idade >=1 && idade <= 5){
    alert('neném')
}else if(idade >=6 && idade<=12){
    alert('Criança')
}else if(idade>=13 && idade<=17){
    alert('Adolescente')
}else if(idade>=18){
    alert('Adulto')
    console.log('Adulto')
}else{
    alert('Eita')
}