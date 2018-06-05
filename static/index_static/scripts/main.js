    function open_tab(event, tab_name)
    {
        let i, tabcontent, tablinks;

        tabcontent = document.getElementsByClassName("tabcontent");
        for (let i = 0; i < tabcontent.length; ++i)
        {
            tabcontent[i].style.display = "none";
        }

        tablinks = document.getElementsByClassName("tablinks");
        for (let i = 0; i < tablinks.length; ++i)
        {
            if(tablinks[i] != event.currentTarget)
            {
                tablinks[i].className = tablinks[i].className.replace("active", "");
            }
        }

        document.getElementById(tab_name).style.display = "block"
        if(event.currentTarget != null && !event.currentTarget.classList.contains("active"))
        {
            event.currentTarget.className += "active";
        }
    }

    let search_form = document.getElementById('search_form') || null;
    function change_action(value)
    {
        if (search_form)
        {
            search_form.action = '/search_' + value
        }
    }