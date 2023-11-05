import frappe
from frappe.desk.desktop import get_workspace_sidebar_items

@frappe.whitelist()
def custom_get_workspace_sidebar_items():
    data = get_workspace_sidebar_items()
    if frappe.local and frappe.local.lang and frappe.local.lang == 'zh':
        trans_map = [
            ['Reports &amp; Masters', '主数据、业务交易、报表'],
            ["Masters &amp; Reports",'主数据、业务交易、报表'],            
            ['Elements', '定制项'],
            ['Quick Access', '快捷方式'],
            ['Your Shortcuts', '快捷方式'],
            ['Settings', '设置'],
            ['Integrations', '应用集成'],
            ['My Workspaces', '我的工作区'],
            ['MY WORKSPACES', '我的工作区'],
            ['Documents', '单据']
        ]
        pages = data.get('pages', [])        
        for page in pages:
            content = page.content
            for (en, zh) in trans_map:
                if content:
                    content = content.replace(en,zh)
            page.content = content                                
    return data


