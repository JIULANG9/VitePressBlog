import { defineConfig } from 'vitepress'

import { withSidebar } from 'vitepress-sidebar';

import XNav from './nav.mjs'

const vitePressOptions = {
  // https://vitepress.dev/reference/site-config
  title: "九狼云墨",
  description: "科技与创意的完美结合",
  documentRootPath: 'docs/post/',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: XNav,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: '©2024 九狼云墨'
    }
  },
  lang: 'zh-CN'
}

const vitePressSidebarOptions = [{
  // VitePress Sidebar's options here..\
  documentRootPath: 'docs/',
  scanStartPath: 'post',
  resolvePath: '/post/',
  collapsed: true,
  capitalizeFirst: true
}];


export default defineConfig(withSidebar(vitePressOptions, vitePressSidebarOptions));