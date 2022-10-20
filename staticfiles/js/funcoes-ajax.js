function utilizou_hora_extra(id){
    console.log(id)
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
        type: 'POST',
        url: '/horas/utilizou_hora_extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (result){
            console.log('sucesso!')
            $('#mensagem').text('foi')
        }
    })
}