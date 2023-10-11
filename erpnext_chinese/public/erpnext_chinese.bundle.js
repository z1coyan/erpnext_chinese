$(document).on('page-change', function() {
    setTimeout(function(){
        if (frappe.boot.lang == 'zh' && frappe.get_route() && 
            (frappe.get_route().at(-1) == 'Workspaces' || frappe.get_route()[0] == 'Workspaces')){
            $('div.ce-block__content span b:contains("报表与主数据")').html("Report and master");
        }
    },
    1000)    
});