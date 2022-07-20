import React, { useContext, useEffect, useState } from 'react'
import '../pagesCSS/Content.css'
import { useNavigate } from 'react-router-dom';

function Content({ content }) {
  const [estado , setEstado] = useState(0)
  const navigate = useNavigate();
  
  const handleClick = (ind) => {
    navigate(`/ler/${content[ind].slug}`)
  }

  return(
    <>
      {content?.map((val, index) => 
        <>        
          <div onClick={() => {
            handleClick(index)
          }}><h1 key={index} className='title'>{val.title}</h1></div>
          <img key={index} className='image' src={val.cover} />
        </>
        
      )}
    
    </>
  )
}

export default Content; 
