import { Link } from 'react-router-dom'
import line from '../img/line.png'
import sun from '../img/sun.png'
import rect from '../img/rect.png'
import { Miniinfo } from '../components/Miniinfo'
import { Card } from 'react-bootstrap'
import { MyCard } from '../components/MyCard'
import React from 'react'

const HomePage = () => {
    class CardHeader extends React.Component {
        render() {
          const { image } = this.props;
          var style = { 
              backgroundImage: 'url(' + image + ')',
          };
          return (
            <header id={image} className="card-header">
                <img src={image} alt="sad" className='cardImage'/>
              {/* <h4 className="card-header--title">News</h4> */}
            </header>
          )
        }
      }
      
    //   class Button extends React.Component {
    //     render() {
    //       return (
    //         <button className="button button-primary">
    //           <i className="fa fa-chevron-right"></i> Find out more
    //         </button>
    //       )
    //     }
    //   }
      
      class CardBody extends React.Component {
        render() {
          return (
            <div className="card-body">
              
              <h2>{this.props.title}</h2>
              
              <p className="body-content">{this.props.text}</p>
              
              {/* <Button /> */}
            </div>
          )
        }
      }
      
      class Card extends React.Component {
        render() {
          return (
            <article className="card">
              <CardHeader image={'https://source.unsplash.com/user/erondu/600x400'}/>
              <CardBody title={'Map'} text={'На данной карте вы можеет увидеть предсказуемые пожары'}/>
            </article>
          )
        }
      }
    return (
        <div>
            <div className='firstBlock'>
                <div className='header'>
                    <h1> lgnis </h1>
                    <img src={line} alt="" className='headerLine'/>
                    <p className='paragraphHeader'>Project that was created to prevent fires and pollution of nature</p>
                </div>
            </div>
            <div className='SecondBlock'>
                <div className='info'>
        
                    <Miniinfo title="760" body="Projects" color="#FF6853" />
                    <Miniinfo title="240+" body="людей спасено" color="#FF537C" />
                    <Miniinfo title="140+" body="пожаров потушено" color="#80D2C4" />
                    <Miniinfo title="3400+" body="спасено деревеьев" color="#3F50E7" />
                    <Miniinfo title="210+" body="пожаров обнуаружено" color="#95CB7C" />
                </div>
                <div className='cards'>
                    <h1 style={{"textAlign":"center", "color":"#D9D9D9", "marginBottom":"100px", "marginTop":"150px"}}>Functions:</h1>
                    <div className='navBlock'>
                        {/* <MyCard title="Map"/>
                        <MyCard title="Map"/>
                        <MyCard title="Map"/>
                        <MyCard title="Map"/> */}
                        <article className="card">
                            <CardHeader image={'https://source.unsplash.com/user/erondu/600x400'}/>
                            <CardBody title={'Map'} text={'На данной карте вы можеет увидеть предсказуемые пожары'}/>
                        </article>
                        <article className="card">
                            <CardHeader image={'https://source.unsplash.com/user/erondu/600x400'}/>
                            <CardBody title={'Map'} text={'На данной карте вы можеет увидеть предсказуемые пожары'}/>
                        </article>
                        <article className="card">
                            <CardHeader image={'https://source.unsplash.com/user/erondu/600x400'}/>
                            <CardBody title={'Map'} text={'На данной карте вы можеет увидеть предсказуемые пожары'}/>
                        </article>
                    </div>
                </div>
                
                <h1>sadasd</h1>
                
            </div>
        </div>
        
    )
}

export {HomePage}