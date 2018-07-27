function setAddress(){
        var ddl=document.getElementById('uni');
        var selOpt=ddl.options[ddl.selectedIndex];
        var uniValue=selOpt.getAttribute('dataind');
        var textBox=document.getElementById('address');
        var cityBox=document.getElementById('city');
        var x=['Z','A', 'B', 'C'];
        var y=['','Normal','Birmingham'];
        textBox.value=x[uniValue];
        cityBox.value=y[uniValue];
        }
