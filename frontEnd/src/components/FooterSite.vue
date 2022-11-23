<template>
    <footer class="footer">
        <div class="container-fluid">
            <p class="text-center">
                <a href="/terms" class="text-green noDecoration"> Termos </a> e <a href="/policy" class="text-green noDecoration">Política </a> | @{{currentYear}} FrontEnd</p>
        </div>
    </footer>
</template>
  
<script>
  export default {
    data() {
      return {
        currentYear: new Date().getFullYear()
      };
    }
  };
</script>