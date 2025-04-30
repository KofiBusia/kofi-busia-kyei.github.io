document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const navLinks = document.querySelectorAll('nav a');
    const header = document.querySelector('header');
    const headerTitle = document.querySelector('header h1');
    const headerSubtitle = document.querySelector('header .subtitle');
    const nav = document.querySelector('nav');
    const headerHeight = header.offsetHeight;
    
    // Set the first link (About) as active by default
    if (navLinks.length > 0) {
        navLinks[0].classList.add('active');
    }
    
    // Function to set active nav link based on scroll position
    function setActiveNavOnScroll() {
        const scrollPosition = window.scrollY;
        
        // Get all sections
        const sections = document.querySelectorAll('section');
        
        // Find the current section
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remove active class from all links
                navLinks.forEach(link => link.classList.remove('active'));
                
                // Add active class to the corresponding nav link
                const activeLink = document.querySelector(`nav a[href="#${sectionId}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }
    
    // Add click event to navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Smooth scroll to the section
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
            
            // Prevent default link behavior
            event.preventDefault();
        });
    });
    
    // Create a fixed navbar that appears on scroll
    // Store original header height for proper spacing
    const originalHeaderHeight = header.offsetHeight;
    let navHeight = nav.offsetHeight;
    let hasScrolled = false;
    
    // Initialize main content padding to prevent jump
    const main = document.querySelector('main');
    
    window.addEventListener('scroll', function() {
        // Update active nav link on scroll
        setActiveNavOnScroll();
        
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // When scrolling down, hide header text and show only navbar
        if (scrollTop > 50) {
            if (!hasScrolled) {
                // Measure nav height before applying fixed positioning
                navHeight = nav.offsetHeight;
                hasScrolled = true;
            }
            
            // Change header appearance using classes instead of inline styles
            header.classList.add('scrolled');
            headerTitle.classList.add('hidden');
            headerSubtitle.classList.add('hidden');
            nav.classList.add('fixed');
            
            // Add padding to main to prevent content jump
            main.style.paddingTop = originalHeaderHeight - navHeight + 'px';
        } else {
            // Reset to original state
            header.classList.remove('scrolled');
            headerTitle.classList.remove('hidden');
            headerSubtitle.classList.remove('hidden');
            nav.classList.remove('fixed');
            
            // Remove padding from main
            main.style.paddingTop = '0';
            hasScrolled = false;
        }
    });
});
