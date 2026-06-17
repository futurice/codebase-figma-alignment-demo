import styles from './Header.module.css'

const links = [
  { label: 'Home', href: '#' },
  { label: 'About', href: '#' },
  { label: 'Contact', href: '#' },
]

export function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>Acme</div>
      <nav className={styles.nav}>
        {links.map((l) => (
          <a key={l.label} href={l.href} className={styles.navLink}>
            {l.label}
          </a>
        ))}
      </nav>
    </header>
  )
}
