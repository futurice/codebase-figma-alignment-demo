import {Button} from '../button/Button'
import styles from './Card.module.css'

type Props = {
  title: string
  description: string
  imageUrl?: string
  buttonLabel?: string
  variant?: 'primary' | 'secondary'
  onAction?: () => void
}

export function Card({
  title,
  description,
  imageUrl,
  buttonLabel = 'Button',
  variant = 'primary',
  onAction,
}: Props) {
  return (
    <article className={styles.card}>
      <div
        className={styles.image}
        style={imageUrl ? { backgroundImage: `url(${imageUrl})` } : undefined}
      />
      <div className={styles.content}>
        <div className={styles.text}>
          <h3 className={styles.title}>{title}</h3>
          <p className={styles.description}>{description}</p>
        </div>
        <div className={styles.actions}>
          <Button variant={variant} onClick={onAction}>
            {buttonLabel}
          </Button>
        </div>
      </div>
    </article>
  )
}
