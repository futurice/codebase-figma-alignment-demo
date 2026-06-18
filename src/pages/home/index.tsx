import {Card} from '../../components/card/Card'
import styles from './index.module.css'

const IMAGE_URL =
  'https://c.pxhere.com/photos/84/ae/Abstract_Artistic_blue_brushstroke_canvas_Creative_Design_Paint-1623557.jpg!d'

const cards = Array.from({ length: 6 }, (_, i) => ({
  id: i + 1,
  title: `Card title ${i + 1}`,
  description: 'Description',
}))

export function Home() {
  return (
    <div className={styles.grid}>
      {cards.map((c, i) => (
        <Card
          key={c.id}
          title={c.title}
          description={c.description}
          imageUrl={IMAGE_URL}
          // TODO design-check: card #3 uses secondary variant; all 6 Figma cards are primary. https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-98
          variant={i === 2 ? 'secondary' :'primary'}
        />
      ))}
    </div>
  )
}

export default Home
