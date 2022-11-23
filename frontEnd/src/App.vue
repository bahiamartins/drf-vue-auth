<template>
  <HeaderSite></HeaderSite>

  <FooterSite></FooterSite>
</template>

<script>
import HeaderSite from '@/components/HeaderSite.vue';
import FooterSite from '@/components/FooterSite.vue'

export default {
    name: 'App',
    components: {
        HeaderSite,
        FooterSite
    },
}
</script>

