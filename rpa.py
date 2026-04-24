from playwright.sync_api import sync_playwright
import re

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Navigate to login page
            page.goto('https://crea.directv.cloud-vsn.com/WebPages/#/login')
            page.get_by_role('textbox', name='User').click()
            page.locator('#email').fill('Fsouza')
            page.get_by_role('textbox', name='Password').click()
            page.locator('#password').fill('F3rn4nd0@1234')
            page.get_by_text('Sign In').click()

            # Navigate to commercials page
            page.goto('https://crea.directv.cloud-vsn.com/WebPages/#/app/commercials/contracts')
            page.get_by_role('link', name=' Broadcast').click()
            page.locator('path').click()
            page.locator('.Select').click()
            page.locator('#react-select-single').fill('gra')
            page.get_by_role('menuitem', name='Gran Hermano - SECONDARY').click()
            page.get_by_role('button', name='April 2026 ').click()
            page.get_by_role('gridcell', name='Feb').click()
            page.locator('#big-calendar-event-f529b36f-04c3-415a-80fd-5719b3cd78d1 > .rbc-event-content').click()
            page.get_by_role('listitem', name='Open Playlist').click()
            page.get_by_text('Automatic Ads Insertion').click()
            page.get_by_role('button', name='Import all').click()

            # Wait for heading
            not_inserted_heading = page.get_by_role('heading', name=re.compile('Not Inserted', re.IGNORECASE))
            not_inserted_heading.first.wait_for(state='visible', timeout=20000)

            # JavaScript evaluation
            total_not_inserted = page.evaluate("""() => {
                function norm(value) {
                    return (value || '').replace(/\\s+/g, ' ').trim();
                }

                function parseIntSafe(value) {
                    const n = parseInt(norm(value).replace(/[^0-9-]/g, ''), 10);
                    return Number.isFinite(n) ? n : 0;
                }

                const tables = Array.from(document.querySelectorAll('table'));

                const targetTable = tables.find((table) => {
                    const cls = (table.className || '').toLowerCase();
                    const text = norm(table.innerText || '');
                    const headers = Array.from(table.querySelectorAll('thead th'))
                        .map((th) => norm(th.textContent || '').toLowerCase());

                    return (
                        cls.includes('failed-list') ||
                        text.toLowerCase().includes('not inserted') ||
                        headers.some((h) => h.includes('not inserted'))
                    );
                });

                if (!targetTable) return 0;

                const rows = Array.from(targetTable.querySelectorAll('tbody tr'));

                return rows.reduce((sum, row) => {
                    const cells = Array.from(row.querySelectorAll('td'));
                    const countCell =
                        row.querySelector('td.count') ||
                        row.querySelector('td[data-id="td_count"]') ||
                        cells[cells.length - 1];

                    return sum + parseIntSafe(countCell?.textContent || '');
                }, 0);
            }""")

            print(f'TOTAL NOT INSERTED = {total_not_inserted}')
            
        except Exception as e:
            print(f'Erro durante execução: {e}')
            raise
        finally:
            browser.close()

if __name__ == '__main__':
    main()
