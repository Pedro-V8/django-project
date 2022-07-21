import React, { useContext, useEffect, useState } from 'react'
import '../pagesCSS/Content.css'
import axios from 'axios';


function LerContent() {
    const [chapters, setChapters] = useState([])

    let caminho = window.location.pathname
    let slug = caminho.substring(5)



    useEffect(() => {
        const asyncFunc = async () => {
            await axios.post('http://127.0.0.1:5000/request_list_chapter', {
                search_site: slug
            }).then((res) => {
                setChapters(res.data)
            })
        }
        asyncFunc()


    }, [])





    return (
        <>
            <h1>HELLO WORLD</h1>
            { }

        </>
    )
}

export default LerContent; 
