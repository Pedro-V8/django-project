import React, { useContext, useEffect, useState } from 'react'
import '../pagesCSS/Content.css'


function LerContent() {
    let caminho = window.location.pathname
    let slug = caminho.substring(5)
    
    console.log(slug)
    return(
        <>
    
            <h1>HELLO WORLD</h1>
    
        </>
    )
}

export default LerContent; 
